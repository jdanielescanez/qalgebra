
import re

rule_circuit = r'(?P<gate_name>[A-Z]+)(?:(?:\_\{(?P<targets>\d+(?::\d+)?(?:,\d+(?::\d+)?)*)\})|(?:\^\{(?P<controls>\d+(?::\d+)?(?:,\d+(?::\d+)?)*)\}))+'
expression_circuit = 'H_{1,2}X_{2}^{1}H_{1,2}'
rule_parametric_circuit = 'H_{\omega,k}X_{k}^{\omega}H_{\omega,k}=X_{\omega}^{k}'

rule_parametric_circuit_re = r'(?P<gate_name>[A-Z]+)(?:(?:\_\{(?P<targets>\\?[a-z]+(?::\\?[a-z]+)?(?:,\\?[a-z]+)*)\})|(?:\^\{(?P<controls>\\?[a-z]+(?::\\?[a-z]+)?(?:,\\?[a-z]+)*)\}))+'
left_side, right_side = rule_parametric_circuit.split('=')

left_side_results = re.findall(rule_parametric_circuit_re, left_side)
right_side_results = re.findall(rule_parametric_circuit_re, right_side)

marked = []

def first_ocurrence_re(x):
  return f'(?P<{x[1:]}>\d+(?:,\d+)*)' if x[0] == '\\' else f'(?P<{x}>\d+)'

def rest_occurrence_re(x):
  name = x[1:] if x[0] == "\\" else x
  return f'(?P={name})'

def get_re(x):
  if not x in marked:
    marked.append(x)
    return first_ocurrence_re(x)
  else:
    return rest_occurrence_re(x)

def format_results(results):
  formatted_results = []
  for i, result in enumerate(results):
    formatted_results.append([])
    name, targets, controls = result
    targets = targets.split(',')
    controls = controls.split(',') if controls != '' else []

    formatted_results[i].append(name)
    formatted_results[i].append(list(map(get_re, targets)))
    formatted_results[i].append(list(map(get_re, controls)))
  
  return formatted_results


left_side_results = format_results(left_side_results)

rule_str_re = ''
for result in left_side_results:
  rule_str_re += result[0] + '\_\{' + ','.join(result[1]) + '\}'
  if len(result[2]) > 0:
    rule_str_re += '\^\{' + ','.join(result[2]) + '\}'

print(rule_str_re)
dic = re.match(rule_str_re, expression_circuit).groupdict()

result_expression = ''
for result in right_side_results:
  result_expression += result[0] + '_{' + ','.join(dic[result[1][1:] if result[1][0] == '\\' else result[1]]) + '}'
  if len(result[2]) > 0:
    result_expression += '^{' + ','.join(dic[result[2][1:] if result[2][0] == '\\' else result[2]]) + '}'

print(expression_circuit)
print(result_expression)
