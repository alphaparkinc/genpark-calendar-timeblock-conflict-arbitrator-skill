from client import CalendarTimeblockConflictArbitratorClient

def main():
    client = CalendarTimeblockConflictArbitratorClient()
    res = client.arbitrate_timeblock_conflicts()
    print('Calendar Conflict Arbitrator: ' + res['arbitration_id'] + ' (' + str(res['duration_minutes']) + 'm)')
    print('Conflict: ' + str(res['conflict_detected']) + ' | Grade: ' + res['timezone_overlap_grade'])
    print('Invite Link: ' + res['calendar_invite_link'])

if __name__ == '__main__':
    main()
