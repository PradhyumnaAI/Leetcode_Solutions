class Solution:

  def countDaysTogether(
      self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
  ) -> int:
    daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    
    def get_day_of_year(date_str: str) -> int:
      parts = date_str.split('-')
      month = int(parts[0])
      day = int(parts[1])
      
      return sum(daysOfMonth[: month - 1]) + day

    
    alice_arrive = get_day_of_year(arriveAlice)
    alice_leave = get_day_of_year(leaveAlice)
    bob_arrive = get_day_of_year(arriveBob)
    bob_leave = get_day_of_year(leaveBob)

   
    if alice_leave < bob_arrive or bob_leave < alice_arrive:
      return 0

    
    start_together = max(alice_arrive, bob_arrive)
    
    end_together = min(alice_leave, bob_leave)

    
    return max(0, end_together - start_together + 1)