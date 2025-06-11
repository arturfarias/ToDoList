import Toast from 'react-native-toast-message';

export const showError = (message: string) => {
  Toast.show({
    type: 'error',
    text1: message,
    position: 'top',
    visibilityTime: 3000,
  });
};

export const showSucess = (message: string) => {
  Toast.show({
    type: 'success',
    text1: message,
    position: 'top',
    visibilityTime: 3000,
  });
};