import { useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';

export function useAccessToken() {
  const [token, setToken] = useState<string>('');

  useEffect(() => {
    const loadToken = async () => {
      const accessToken = await AsyncStorage.getItem('accessToken');
      if (accessToken) setToken(accessToken);
    };
    loadToken();
  }, []);

  return token;
}