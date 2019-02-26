# Support file to run solr server and location-plotter server
import os,sys,signal

solrpath = os.getcwd() + "/solr/bin/"
locserverpath = os.getcwd() + "/location-plotter/"

def exitfunc(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    signal.signal(signal.SIGINT, original_sigint)

    try:
        print("\n\nBye, setting server down...")
        os.chdir(solrpath)
        os.system(r"solr stop -all")

    except KeyboardInterrupt:
        sys.exit(1)

    # restore the exit gracefully handler here    
    signal.signal(signal.SIGINT, exitfunc)

if __name__ == '__main__':
    print(''' 
                       ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'    Ground Assist Core
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'         
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'              Devs - Deepak Balhara
   `&%\ ` /%&'    |.|        \ '|8'                       Sarthak Rohilla
       |o|        | |         | |
       |.|        | |         | |
    \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
     ''')
    print("\nUrl for dashboard\n\n'http://localhost:8983/solr/banana/src/index.html#/dashboard/solr/Forest%20Data%20Analytics?server=%2Fsolr%2F'\n")
    try:
        original_sigint = signal.getsignal(signal.SIGINT)
        signal.signal(signal.SIGINT, exitfunc)
        # For running solr server as background
        os.chdir(solrpath)
        os.system(r"solr start")

        #For running location-plotter server
        os.chdir(locserverpath)
        os.system("py manage.py runserver")
    except Exception as e:
        print("\nsomething happened.....")
        sys.exit(1)
