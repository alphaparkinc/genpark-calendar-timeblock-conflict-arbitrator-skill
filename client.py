class CalendarTimeblockConflictArbitratorClient:
    def arbitrate_timeblock_conflicts(self, proposed_start_iso='2026-09-07T14:00:00Z', duration_minutes=45, attendee_timezones=['America/Los_Angeles', 'Asia/Tokyo', 'Europe/London']):
        return {
            'arbitration_id': 'cal_arb_3301',
            'proposed_start': proposed_start_iso,
            'duration_minutes': duration_minutes,
            'attendees_count': len(attendee_timezones),
            'conflict_detected': False,
            'timezone_overlap_grade': 'OPTIMAL_BUSINESS_HOURS',
            'protected_deep_work_preserved_hours': 3.5,
            'recommended_slot_iso': proposed_start_iso,
            'calendar_invite_link': 'https://productivity.developer.genpark.ai/calendar/invite/cal_arb_3301.ics'
        }
