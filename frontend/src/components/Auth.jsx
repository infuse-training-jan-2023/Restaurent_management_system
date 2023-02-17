import React from "react";

import { useState, useEffect } from "react";

const useAuth = () => {
  const [user, setUser] = useState(null);
  const signIn = (username) => {
    setUser(username);
  };

  const signOut = () => {
    setUser(null);
  };

  return { user, signIn, signOut };
};
export default useAuth;
