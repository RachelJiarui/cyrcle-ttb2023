import './App.css';
import React, { useState } from 'react';

const App = async () => {
  const getData = async () => {
    const response = await fetch(`http://127.0.0.1:5000/getfriends`);
    const data = await response.json(); // changes into json object
    const make_friends_list = Object.values(data);

    /*console.log(make_friends_list.length);
    for(let i = 0; i < make_friends_list.length; i++){
      let friend = make_friends_list[i];
      console.log(friend['name']);
    }*/

    //return data['results']; // draw out the elements and set to state
    return make_friends_list // returns an array of the stuff in the friend_dict 
  };

  let response = await getData();

  const name = "";
  const location = "";
  const interests = [];

  const [user_num, set_user_num] = useState(0);
  const nextUser = () => {
      set_user_num(prev => (prev + 1) % response.length)
  }

  let view_friend = response[user_num];
  console.log(view_friend['id']);

  name = view_friend['name'];
  location = view_friend['location'];
  interests = view_friend['interests'];

  return (
    <button onClick={nextUser}>{name} hi</button>
  );
}

export default App;
