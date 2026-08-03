class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        cars = list(zip(position, speed))
        cars.sort(reverse = True)

        for pos, spd in cars:
            time = (target-pos)/spd
            if not fleet or time > fleet[-1]:
                fleet.append(time)
        
        return len(fleet)
        