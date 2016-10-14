__author__ = 'XiaochengWen'
class Solution(object):
    def reconstructQueue(self, people):
        temp = [[] for i in range(1100)]
        out = []
        maxhign = 0
        for i in people:
            temp[i[1]].append(i[0])
            if i[1]>maxhign:
                maxhign = i[1]
        temp[0].sort()
        for i in temp[0]:
            out.append([i,0])
        for i in range(1,maxhign+1):
            temp[i].sort(reverse=True)
            for j in temp[i]:
                higher = i
                index = 0
                while higher>0:
                    if out[index][0]>=j:
                        higher -= 1
                    index += 1
                out.insert(index,[j,i])
        return out


class Solution1(object):
    def reconstructQueue(self, people):
        if not people: return []

        peopledct, height, out = {}, [], []

        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],

        height.sort(reverse=True)  # here are different heights we have

        # sort from the tallest group
        for h in height:
            peopledct[h].sort()
            for p in peopledct[h]:
                out.insert(p[0], people[p[1]])
        return out






