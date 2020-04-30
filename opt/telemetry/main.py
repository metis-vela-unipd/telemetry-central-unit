from sensors_provider import SensorsProvider
from webapp import Webapp
from colorama import Fore, Style
from logger import Logger


# Start the data provider thread (actually is only the gpsd thread)
provider = SensorsProvider()
provider.start()

# Start the logger thread
logger = Logger(provider)
logger.start()

# Start the web thread
webapp = Webapp(provider, logger)
webapp.start()

# Wait until all the threads have finished initializing (or exit after timeout)
provider.end_setup.wait(timeout=20)
webapp.end_setup.wait(timeout=20)
logger.end_setup.wait(timeout=20)

if not provider.end_setup.isSet() or \
   not webapp.end_setup.isSet() or \
   not logger.end_setup.isSet():
    print(f"{Fore.RED}[main_thread] Something went wrong during threads initialization, quitting...{Fore.RESET}")
    exit(1)

# Wait all threads to start
print(f"{Style.BRIGHT}[main_thread] Telemetry system started (CTRL+C to stop){Style.RESET_ALL}")

# Watch threads and try recovery when needed, terminate program when KeyboardInterrupt is caught
while True:
    try:
        if not provider.is_alive():
            print(f"{Fore.YELLOW}[main_thread] Provider dead, attempting recovery...{Fore.RESET}")
            provider = SensorsProvider()
            provider.start()
            provider.end_setup.wait(timeout=20)
            if provider.end_setup.isSet():
                webapp.provider = provider.get_sensor('gps')
                print(f"{Fore.GREEN}[main_thread] Done recovery!{Fore.RESET}")
            else:
                print(f"{Fore.RED}[main_thread] Recovery failed, quitting...{Fore.RESET}")
                exit(1)
    except KeyboardInterrupt:
        print(f"{Fore.RED}[main_thread] KeyboardInterrupt caught, quitting...{Fore.RESET}")
        exit(0)
