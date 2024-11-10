from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# import urllib
# url = "https://servif.insa-lyon.fr/EdT/3IF"
# urllib.urlretrieve(url, "EdT.html")

# Function to decode hexadecimal titles


def decode_title(hex_title):
    hex_str = hex_title.split('-')[1]
    bytes_object = bytes.fromhex(hex_str)
    return bytes_object.decode('utf-8')

# Function to Condense the JSON slots


def condense_slots(cells):
    condensed_slots = []
    temp_slot = {}

    for cell in cells:
        if cell['id']:
            i = 0
            dur = 0

            temp_class = []
            temp_class.append(cell['class'][0][5:])
            temp_class.append(decode_title(cell['class'][1]))

            span = int(cell['colspan'])
            id = cell['id'][:-2]

            if span == 4:
                dur = 4
            elif span > 4:
                dur = span - 1
            elif span > 9:
                dur = span - 2
            elif span > 13:
                dur = span - 3
            elif span > 17:
                dur = span - 3
            elif id[-2:].split('-')[0] % 5 + span > 4:
                dur = span-1
            elif id[-2:].split('-')[0] % 5 + span > 9:
                dur = span - 2
            elif id[-2:].split('-')[0] % 5 + span > 13:
                dur = span - 3
            elif id[-2:].split('-')[0] % 5 + span > 17:
                dur = span - 4
            else:
                dur = span

            temp_slot = {
                'id': id,
                'colspan': cell['colspan'],
                'rowspan': cell['rowspan'],
                'class': temp_class,
                'content': cell['content'],
                'start': "",
                'dur': dur,
                'name': "",
                'pos': "",
                'prof': ""
            }
        else:
            if i == 0:
                temp_slot['name'] = cell['content']
                i += 1
            elif i == 1:
                temp_slot['pos'] = cell['content'][8:]
                temp_slot['start'] = cell['content'][:5]
                i += 1
            elif i == 2:
                temp_slot['prof'] = cell['content']
                condensed_slots.append(temp_slot)

    return condensed_slots

# Function to calculate yeardays from weekdays


def get_date_from_week_day(year, week, day):
    # Calculate the first day of the year
    first_day_of_year = datetime(year, 1, 1)

    # Calculate the first Monday of the year
    first_monday = first_day_of_year + \
        timedelta(days=(7 - first_day_of_year.weekday()))

    # Calculate the date based on the week and day
    event_date = first_monday + timedelta(weeks=week-1, days=day-1)

    return event_date.date()

# Function to convert cJSON event to iCal format


def json_to_ical(events):
    curr_year = 2024  # Change in 2025 ;)
    last_week = 1

    ical_events = []
    for event in events:

        # Extract week and day from the id
        week = int(event['id'].split('-')[1][1:])
        day = int(event['id'].split('-')[2][1:])

        if last_week > week:
            curr_year += 1
        # Calculate the event date
        event_date = get_date_from_week_day(curr_year, week, day)

        # Parse start time and calculate end time
        start_time = datetime.strptime(event['start'], "%Hh%M").time()
        start_datetime = datetime.combine(event_date, start_time)
        duration = timedelta(minutes=event['dur'] * 15)
        end_datetime = start_datetime + duration

    # Get current time for DTSTAMP
        dtstamp = datetime.now().strftime('%Y%m%dT%H%M%S')

        # Create iCal event
        ical_event = f"""BEGIN:VEVENT
UID:{event['id']}
DTSTART:{start_datetime.strftime('%Y%m%dT%H%M%S')}
DTEND:{end_datetime.strftime('%Y%m%dT%H%M%S')}
DTSTAMP:{dtstamp}
SUMMARY:{event['name']}
LOCATION:{event['pos']}
DESCRIPTION:Professor: {event['prof']}
END:VEVENT"""
        ical_events.append(ical_event)
        last_week = week

    return "\n".join(ical_events)


# Read HTML file
with open('EdT.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract data
data = []
for tr in soup.find_all('tr', class_='hour'):
    row_data = {}
    row_data['class'] = tr.get('class')
    row_data['headers'] = [th.get_text(strip=True).replace(
        '\u00a0', ' ') for th in tr.find_all('th')][:2]

    row_data['cells'] = []

    # Skip other groups TEMPORAL!
    if row_data['class'][1] in ["row-group-2", "row-group-3", "row-group-4"]:
        continue

    for td in tr.find_all('td'):
        cell_data = {
            'id': td.get('id'),
            'colspan': td.get('colspan'),
            'rowspan': td.get('rowspan'),
            'class': td.get('class'),
            'content': td.get_text(strip=True).replace('\u00a0', ' ')
        }

        if cell_data['class'] == ['NOSLOT']:  # Skip NOSLOT slots
            continue

        row_data['cells'].append(cell_data)
    data.append(row_data)

# Convert to JSON with ensure_ascii=False to handle Unicode characters
json_data = data

# Condense the slots in the data
for day in json_data:
    if 'cells' in day:
        day['cells'] = condense_slots(day['cells'])

events = []
for day in json_data:
    if 'cells' in day:
        events.extend(day['cells'])

# Convert events to iCal format
ical_data = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//INSA/IF3/1
{json_to_ical(events)}
END:VCALENDAR"""

# Save iCal data to .ics file
with open('schedule.ics', 'w', encoding='utf-8') as file:
    file.write(ical_data)

print("iCal file created successfully.")
