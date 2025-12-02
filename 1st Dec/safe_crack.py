def safe_cracker(start_position: int) -> int:
  
  # Transform list of instructions into a list of positive/negative values    
  instructions = get_instructions()
  movements = [movement_helper(item) for item in instructions]
  
  zero_count = 0
  position = start_position
  
  # Works out the next position, if 0 it increments the count
  for value in movements:
    position = (position + value) % 100
    if position == 0:
      zero_count += 1
    
  return zero_count

# Gets instructions from a file
def get_instructions() -> list[str]:
  # Start by reading lines from the input file
  with open("input.txt", "r") as file:
      return file.readlines()
      

# Converts an instruction to a positive or negative number (e.g. L4 becomes -4, R5 becomes 5)
def movement_helper(instruction: str) -> int: # pyright: ignore[reportReturnType]
  # We can assume a consitent format (L__ R__) where there only numbers after an L or R
  match instruction[0]: # pyright: ignore[reportMatchNotExhaustive]
    case "L":
      return 0 - int(instruction[1:])
    case "R":
      return int(instruction[1:])
    
if __name__ == '__main__':
  print(
    safe_cracker(50)
  )