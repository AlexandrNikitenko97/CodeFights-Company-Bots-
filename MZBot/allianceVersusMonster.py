def allianceVersusMonster(healthPoints, attackDamage):
    monsterHp = healthPoints[0]              # Monster health
    monsterDg = attackDamage[0]              # Monster damage
    healthPoints = healthPoints[1:]          # Alliance warriors health
    attackDamage = attackDamage[1:]          # Alliacne warriors damage
    hurtedWarriors = []                      # Array for hurted wariors health after attack
    hurtedWarriorsDamag = []                 # Array for hurted wariors damage after attack
    while monsterHp > 0:
      
        # Find warrior with optimal health or punch
      
        if len(healthPoints) != 0:
            if max(attackDamage) >= monsterHp:
                damage = attackDamage.index(max(attackDamage))
            else:
                damage = healthPoints.index(max(healthPoints))
            punch = healthPoints[damage] // monsterDg
            if punch >= healthPoints[damage]:
                punch -= 1
            monsterHp -= punch * attackDamage[damage]
        elif len(hurtedWarriorsDamag) != 0:
            if max(hurtedWarriorsDamag) >= monsterHp:
                damage = hurtedWarriorsDamag.index(max(hurtedWarriorsDamag))
            else:
                damage = hurtedWarriors.index(max(hurtedWarriors))
            monsterHp -= hurtedWarriorsDamag[damage]
        else: 
            return 0
            
        # Return the length of arrays with warriors of the monster is dead
            
        if monsterHp <= 0:
            return len(healthPoints) + len(hurtedWarriors) if len(healthPoints) != 0 else len(hurtedWarriors)
        else:
            if len(healthPoints) != 0:
                healthPoints[damage] -= punch * monsterDg
                if healthPoints[damage] > 0:
                    # Move warrior health and damage to 'hurt' array after attack
                    hurtedWarriors.append(healthPoints[damage])        
                    hurtedWarriorsDamag.append(attackDamage[damage])
                del healthPoints[damage]
                del attackDamage[damage]
            else:
                # If warrior is dead than delete him from array 
                del hurtedWarriors[damage]
                del hurtedWarriorsDamag[damage]
