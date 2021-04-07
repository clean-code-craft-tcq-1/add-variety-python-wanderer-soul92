def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


cooling_type =  { 'PASSIVE_COOLING': {'lowerLimit': 0,'upperLimit':35},
                     'HI_ACTIVE_COOLING': {'lowerLimit': 0,'upperLimit':45},
                     'MED_ACTIVE_COOLING': {'lowerLimit': 0,'upperLimit':40}
                   }

Email_alert = { 'TOO_LOW' : {'Recepient':'a.b@c.com', 'Message':'Hi, the temperature is too low'},
                'TOO_HIGH' : {'Recepient':'a.b@c.com', 'Message':'Hi, the temperature is too high'}
            }

def classify_temperature_breach(coolingType, temperatureInC):
    lowerLimit = cooling_type[coolingType]['lowerLimit']
    upperLimit = cooling_type[coolingType]['upperLimit']
    return infer_breach(temperatureInC, lowerLimit, upperLimit)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar, temperatureInC)
  if alertTarget in Alert_Target.keys():
      Alert_Target[alertTarget](breachType)
  return breachType

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
    print(f'{Email_alert[breachType]}')
  
def send_to_console(breachType):
    header = 0xfeed
    print(f'{header}, {breachType}')

Alert_Target = { 'TO_CONTROLLER': send_to_controller,
                'TO_EMAIL': send_to_email,
                'TO_CONSOLE': send_to_console }