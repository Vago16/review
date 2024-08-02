const dt = new Date();
const month = dt.getMonth();
let msg;

switch (month) {
    case 0:
        msg = 'January 4 is National Spaghetti Day!';
            break;
    case 1:
        msg = 'February 9 is National Pizza Day!';
            break;
    case 2:
        msg = 'March 26 is National Spinach Day!';
            break;
    case 3:
        msg = 'April 26 is National Pretzel Day!';
        break;
    default:
        msg = 'I am too lazy to list out the rest of the months.';
    }

const el = document.getElementById('message');
el.innerHTML = msg

