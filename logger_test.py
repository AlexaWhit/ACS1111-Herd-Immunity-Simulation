from logger import Logger

log_test = Logger('log_test.txt')
log_test.write_metadata(2500, 0.6, "SARS", 0.4, 0.6)
log_test.log_interactions()