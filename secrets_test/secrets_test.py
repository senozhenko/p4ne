from redminelib import Redmine

# disable insecure warnings
requests.packages.urllib3.disable_warnings()


BASE_URL = demisto.params().get('URL')
SSL_VERIFY = demisto.params().get('ssl_verify')
API_KEY = P@ssw0rd
#API_KEY = demisto.params().get('apikey')

input: |
  dbusername = admin
  dbpassword = 8095uohoiw4ur90
  dbhost = db-postgres-nyc1-1111-do-user-111111-0.db.ondigitalocean.com
  dbport = 25060
  dbdatabase = defaultdb
  dbsslmode = require
output:
  username: admin
  password: 8095uohoiw4ur90
  host: db-postgres-nyc1-1111-do-user-111111-0.db.ondigitalocean.com
  port: 25060




def redmine_auth():
    redmine = Redmine(BASE_URL, key=API_KEY, requests={'verify': SSL_VERIFY})
    return redmine

def create_command():
    args = demisto.args().get('create')
    arg_subject = demisto.args().get('subject', 'default subject')
    arg_description = demisto.args().get('description', 'Empty')
    redmine = redmine_auth()
    create = redmine.issue.create(project_id='git-helloworld',
                                    subject=arg_subject,
                                    description=arg_description)






''' EXECUTION '''
LOG('command is %s' % (demisto.command(), ))
try:
    if demisto.command() == 'test-module':
        demisto.results('ok')
        sys.exit(0)
    elif demisto.command() == 'RedMine-create':
        create_command()
        demisto.results({'status': 'Issue has been created', 'qwe':123})
    else:
        demisto.results('Unknown command')
except Exception as e:
    demisto.debug('The Senate? I am the Senate!')
    LOG(str(e))
    LOG.print_log()
    return_error(str(e))
