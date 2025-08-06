import { log } from 'console';

interface UserProfile {
  firstName: string;
  middleName?: string;
  lastName: string;
}

const user1: UserProfile = { 
  firstName: 'Nicolás', 
  middleName: 'Alberto', 
  lastName: 'Córdoba' 
};

const user2: UserProfile = { 
  firstName: 'Alan', 
  lastName: 'Turing' 
};


function createUserGreeting(
  firstName: string, 
  salutation: string = "Hello",
  middleName?: string
) {
  var message = `[${salutation}], [${firstName}]`;
  return middleName ? `${message} [${middleName}]!` : `${message}!`;
  // return message + middleName ? ` [${middleName}]!` : '!';
}

log(createUserGreeting(user1.firstName, 'Hello', user1.middleName));
log(createUserGreeting(user2.firstName, 'Hello'));