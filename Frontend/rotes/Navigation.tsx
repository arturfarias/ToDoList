import React from 'react';
import { StyleSheet } from 'react-native';

import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import Login from '../screens/Login';
import Register from '../screens/Register';
import Home from '../screens/Home';

export type Pages = {
  Login: undefined;
  Register: undefined;
  Home: undefined;
}

const Stack = createStackNavigator<Pages>();

const Navigation: React.FC = () => {

  return (
    <NavigationContainer>
        <Stack.Navigator 
          initialRouteName='Login'
          
          screenOptions={{ 
            headerStyle: styles.header,
            headerShadowVisible: false,
            headerTintColor: '#fff',
          }}
        >
            <Stack.Screen 
                name='Login'
                options={{ headerShown: false }}
                component={Login}
            />
            <Stack.Screen 
                name='Register' 
                component={Register}
                options={{ title: 'Cadastro' }}
            />
            <Stack.Screen 
                name='Home'
                options={{ headerShown: false }}
                component={Home}
            />
        </Stack.Navigator>
    </NavigationContainer>
  );
};

const styles = StyleSheet.create({
  header: {
    backgroundColor: '#6a0dad',
    elevation: 0,
    shadowOpacity: 0,
    borderBottomWidth: 0,
  },
});

export default Navigation;