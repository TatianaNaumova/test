import sys
import json

def fill_values(tests, values):
  if "values" in tests.keys():
    for test in tests["values"]:
      fill_values(test, values)
  
  id = tests["id"]
  
  for result in values["values"]:
    if result["id"] == id:
      tests["value"] = result["value"]
      break
  return tests


if __name__ == "__main__": 
  tests_filename = sys.argv[1]
  values_filename = sys.argv[2]
  tests_file = open(tests_filename, "r")
  tests_dict = json.load(tests_file)
  tests_file.close()
  
  values_file = open(values_filename, "r")
  values_dict = json.load(values_file)
  values_file.close()
  
  result_dict = fill_values(tests_dict, values_dict)
  result_json = json.dumps(result_dict)
  
  result_file = open("result.json", "w")
  result_file.write(result_json)
  result_file.close()   
