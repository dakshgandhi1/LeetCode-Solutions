class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiant = []
        dire = []
        for ind,char in enumerate(senate):
            if char == 'R':
                radiant.append(ind)
            else:
                dire.append(ind)
        n = len(senate)
        while len(radiant) > 0 and len(dire) > 0:        
            if radiant[0] < dire[0]:
                radiant.pop(0)
                dire.pop(0)
                radiant.append(n)
                n += 1
            else:
                radiant.pop(0)
                dire.pop(0)
                dire.append(n)
                n += 1
        if len(dire) == 0:
            return "Radiant"
        else:
            return "Dire"

        