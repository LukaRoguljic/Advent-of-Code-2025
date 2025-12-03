def aocp2(instructions):
  position = 50
  zero_hits = 0
  remainder = 0
  old = 50

  for instruction in instructions:
    direction = instruction[0]
    distance = int(instruction[1:])

    full_cycle = (distance // 100)
    if(full_cycle > 0):
      zero_hits = zero_hits + full_cycle
    
    remainder = distance % 100
    old = position

    if direction == 'R': 
      if ((old + remainder)) >= 100:
        zero_hits = zero_hits + 1
      position = (old + remainder) % 100

    if direction == 'L':
      if old != 0 and (old - remainder) <= 0:
        zero_hits = zero_hits + 1
      position = (old - remainder) % 100

  return zero_hits

