# Name : Anish Banswada

# Strategy : Maintain 2 heaps

# Time Taken : 40 minutes

# Assumptions : Only dogs and cats are inserted and adopted

# Space Complexity : O(n)

# Time Complexity :  O(nlogn) for initialization, O(log n) for insert and adopt 
import heapq
# Function 
class AdoptionCenter:
    def __init__(self,pets):
        self.cats = []
        self.dogs = []
        self.day = 1
        for item in pets:
            name = item[0]
            time = item[2]
            if item[1] == 'dog':
                heapq.heappush(self.dogs,(-time,name))
            else:
                heapq.heappush(self.cats,(-time,name))
    def adopt(self,preference):
        if preference == 'dog':
            if not self.dogs:
                if not self.cats:
                    return 'No pets available'
                time,name = heapq.heappop(self.cats)
                return name + ' cat'
            time,name = heapq.heappop(self.dogs)
            return name + ' dog'
        else:
            if not self.cats:
                if not self.dogs:
                    return ('No pets available')
                    
                time,name = heapq.heappop(self.dogs)
                return name + ' dog'
            time,name = heapq.heappop(self.cats)
            return name + ' cat' 
    def insert(self,name,species):
        if species == 'dog':
            heapq.heappush(self.dogs,(self.day,name))
        else:
            heapq.heappush(self.cats,(self.day,name))
        self.day += 1

        
# Main

if __name__ == "__main__":
    pets = [['Sadie', 'dog', 4],
['Woof', 'cat', 7],
['Chirpy', 'dog', 2],
['Lola', 'dog', 1],
]
    res = AdoptionCenter(pets)
    assert res.adopt('dog') == 'Sadie dog'
    res.insert('Floofy','cat')
    assert res.adopt('cat') == 'Woof cat'
    assert res.adopt('cat') ==  'Floofy cat'
    assert res.adopt('cat') == 'Chirpy dog'
    print('Testing completed')
   
 