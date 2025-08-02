type UserID = number;
type UserContact = [string, number];

// Data for the user profile
const userID: number = 101;
const userName: string = "alex_jones";
const isUserActive: boolean = true;
const userContacts: [string, number][] = [
    ["alex.jones@example.com", 1234567890],
    ["secondary.aj@work.com", 9876543210]
];

const userProfile: 
    { 
        id: UserID, 
        userName: string, 
        contacts: UserContact[]
    } = {
        id: userID,
        userName: userName,
        contacts: userContacts
    }