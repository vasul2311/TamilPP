dictionary = {
    # Conditionals (நிபந்தனைகள்)
    'எனில்': 'if', 'enil': 'if', 'if': 'if',
    'ஆனால்': 'elif', 'aanaal': 'elif', 'elif': 'elif',
    'இல்லை': 'else', 'illai': 'else', 'else': 'else',
    
    # Loops (சுழல்கள்)
    'சுற்று': 'for', 'sutru': 'for', 'for': 'for',
    'வரை': 'while', 'varai': 'while', 'while': 'while',
    'வீச்சு': 'range', 'veechu': 'range', 'range': 'range', # NEW: for looping a specific number of times
    
    # Flow Control (கட்டுப்பாட்டு வார்த்தைகள்)
    'நிறுத்து': 'break', 'niruthu': 'break', 'stop': 'break',
    'தொடர்': 'continue', 'thodar': 'continue', 'continue' : 'continue',
    
    # Logical & Membership Operators (தருக்க மற்றும் உறுப்பினர் வார்த்தைகள்)
    'மற்றும்': 'and', 'matrum': 'and', 'and': 'and',
    'அல்லது': 'or', 'allathu': 'or', 'or': 'or',
    'அல்ல': 'not', 'alla': 'not', 'illatha': 'not', 'not': 'not', # NEW
    'இல்': 'in', 'il': 'in', 'in': 'in', # NEW: used in for loops (e.g., x in list)
    
    # Booleans & Null (உண்மை/பொய்/வெற்று)
    'உண்மை': 'True', 'unmai': 'True', 'true': 'True',
    'பொய்': 'False', 'poi': 'False', 'false': 'False',
    'ஏதுமில்லை': 'None', 'ethumillai': 'None', 'vetru': 'None', 'none': 'None', # NEW
    
    # Functions & Classes (செயல்பாடுகள் மற்றும் வகுப்புகள்)
    'செயல்': 'def', 'seyal': 'def', 'def': 'def',
    'திருப்பு': 'return', 'thiruppu': 'return', 'return': 'return',
    'வகுப்பு': 'class', 'vaguppu': 'class', 'class': 'class', # NEW: Object Oriented Programming
    
    # Data Types & Casting (தரவு வகைகள்) - NEW SECTION
    'முழுஎண்': 'int', 'muzhuen': 'int', 'int': 'int',
    'சரம்': 'str', 'saram': 'str', 'str': 'str',
    'தசமம்': 'float', 'thasamam': 'float', 'float': 'float',
    'பட்டியல்': 'list', 'pattiyal': 'list', 'list': 'list',
    'அகராதி': 'dict', 'agaraathi': 'dict', 'dict': 'dict',
    
    # Built-in Functions (உள்ளமைக்கப்பட்ட செயல்பாடுகள்) - NEW SECTION
    'நீளம்': 'len', 'neelam': 'len', 'len': 'len',
    
    # I/O (உள்ளீடு/வெளியீடு)
    'பதி': 'print', 'pathi': 'print', 'padi': 'print', 'print': 'print',
    'உள்ளிடு': 'input', 'ullidu': 'input', 'input': 'input',
    
    # Modules / Imports (தொகுதிகள்) - NEW SECTION
    'இறக்குமதி': 'import', 'irakkumathi': 'import', 'import': 'import'
}
