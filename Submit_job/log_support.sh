#!/bin/bash
 
##  Some simple helper log functions to track jobs success / failure   ##
## Created by Dane Kennedy @ the Centre for High Performance Computing ##
 
############## Create some useful functions ##############
 
# Echos the current date/time in a nice format
function now { echo -n "$( date +"%F %X" )"; }
 
# Appends to log file
function log () {
  if [[ -v LOGFILE ]]
  then
    echo -e "$( now ): ${HOSTNAME}: $@" >> "${LOGFILE}"
  else
    echo -e "$( now ): ${HOSTNAME}: $@"
  fi
}
 
#Appends to log file and exits
function log_fail () {
  log "$@"
  exit 1
}
 
# returns true (in the bash sense of 0 exit status meaning success) if line exists in log file
function check_log () {
  if [[ -v LOGFILE ]]
  then
    if [[ -e ${LOGFILE} ]]
    then
      if $( grep -q "$@" ${LOGFILE} )
      then
        return 0
      fi
    fi
  fi
  return 1
}
 
# Checks for a line on the LOG file. If is exists, it doesn't repeat. If it's not there, it runs. If
# the run is successful is records it as such.
function check_run (){
  SUCCESS_LINE="\"$@\" SUCCESSUL"
  FAIL_LINE="\"$@\" fail."
  if check_log "${SUCCESS_LINE}"
  then
    log "\"$@\" already successfully run. Not repeating."
    return 0
  fi
  log "Running \"$@\""
  $@ \
    && { log "${SUCCESS_LINE}"; return 0; } \
    || { log "${FAIL_LINE}"; return 1; }
}
 
 
# Same as above but exit 1's on fail.
function check_run_abort (){
  if ! check_run "$@"
  then
    log "Aborting."
  fi
}
