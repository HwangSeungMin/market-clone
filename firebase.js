import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
import { getStorage } from "firebase/storage";
import { getAuth } from "firebase/auth";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  apiKey: "AIzaSyBKxEC4yWVcIBZENWCmjjwK8xKiF-FcXCM",
  authDomain: "carrot-market-240516.firebaseapp.com",
  databaseURL:
    "https://carrot-market-240516-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "carrot-market-240516",
  storageBucket: "carrot-market-240516.appspot.com",
  messagingSenderId: "924609013530",
  appId: "1:924609013530:web:9c294c7821c5780c04aea3",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);
const storage = getStorage(app);
const Auth = getAuth(app);
