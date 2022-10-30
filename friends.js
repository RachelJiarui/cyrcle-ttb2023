var friend1 = {
    fullName: 'Juliette Mangon',
    age: '18',
    occupation: 'Syracuse Student',
    mutual: 'Rachel Chen'
};

var friend2 = {
    fullName: 'Aria Maher',
    age: '18',
    occupation: 'Washington University Student',
    mutual: 'Charlie Huang'
};

var friend3 = {
    fullName: 'Saumith Menon',
    age: '18',
    occupation: 'Premed Student',
    mutual: 'Michelle Wu'
};

const allFriends = [friend1, friend2, friend3]
var friendIndex = 0;

function changeFriend()
        {
                let friend = allFriends[friendIndex];

                document.getElementById('name').innerHTML = friend['fullName'];
                document.getElementById('age').innerHTML = friend['age'];
                document.getElementById('occupation').innerHTML = friend['occupation'];
                document.getElementById('mutual').innerHTML = friend['mutual'];

                friendIndex = (friendIndex + 1) % allFriends.length;
        }