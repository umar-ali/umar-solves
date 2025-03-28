def Solution(contributers, projects):
    answer = dict()
    contributers_names = list(contributers.keys())
    projects_names = list(projects.keys())
    for proj in projects_names:
        assigned_contributers = []  
        for i in projects[proj]['requiredskills'].items():
            name,level = i
            for j,k in contributers.items():
                if name in k.keys() and k[name] >= level:
                    assigned_contributers.append(j)
                    if k[name] == level:
                       k[name] += 1 
        if len(assigned_contributers) > 0:
            answer[proj] = assigned_contributers
        
    
    for project, names in answer.items():
        if len(names) != len(projects[project]["requiredskills"].items()):
            return Solution(contributers, projects)
        return answer


    

    
contributers = dict()
projects = dict()                
if __name__ =='__main__':
    
    with open("C:/python/py39/Google Hash Code/mentor&teamwork/inputs/a_an_example.in.txt",'r+') as f:
        No_of_contributers, No_of_projects = tuple(map(int,f.readline().split()))
        for i in range(No_of_contributers):
            name, skills = tuple(f.readline().split())
            skillset = dict()
            for j in range(int(skills)):
                skill, level = tuple(f.readline().split())
                skillset[skill] = int(level)
            contributers[name] = skillset
        for i in range(No_of_projects):
            name, days , score, bestbefore, No_of_requiredskills = tuple(f.readline().split())
            required_skillset = dict()
            for j in range(int(No_of_requiredskills)):
                skill, level = tuple(f.readline().split())
                required_skillset[skill] = int(level)
            projects[name] = {'days': int(days), 'score': int(score), 'bestbefore':int(bestbefore),"requiredskills":required_skillset}
    f.close()
    sol = Solution(contributers, projects)
    with open("C:/python/py39/Google Hash Code/mentor&teamwork/submissions/a_an_example.out.txt",'w+') as f:
        f.write(str(len(sol.items()))+'\n')
        for i,j in sol.items():
            f.write(i+"\n")
            f.write(' '.join(j)+"\n")
    f.close()



