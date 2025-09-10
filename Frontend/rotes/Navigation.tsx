import React from 'react';
import { StyleSheet } from 'react-native';

import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Ionicons from 'react-native-vector-icons/Ionicons';

import Login from '../screens/Login';
import Register from '../screens/Register';
import Home from '../screens/Home';
import Profile from '../screens/Profile';

export type PagesStack = {
  Login: undefined;
  Register: undefined;
  Home: undefined;
}

export type PagesTabs = {
  ToDo: undefined;
  Tarefa: undefined;
  Perfil: undefined;
}

const Stack = createStackNavigator<PagesStack>();
const Tab = createBottomTabNavigator<PagesTabs>();

function Tabs() {
  return (
    <Tab.Navigator
      screenOptions={{
        headerStyle: styles.header,
        headerShadowVisible: false,
        headerTintColor: '#fff',
        tabBarActiveTintColor: '#6a0dad',
      }}
    >
      <Tab.Screen name="ToDo" component={Home}
          options={{
          tabBarIcon: ({ color, size }) => (
            <Ionicons name="list-circle-outline" size={24} color={color} />
          )
        }}
      /> 
      <Tab.Screen name="Tarefa" component={Home}
          options={{
          tabBarIcon: ({ color, size }) => (
            <Ionicons name="add-circle-outline" size={24} color={color} />
          )
        }}
      /> 
      <Tab.Screen name="Perfil" component={Profile}
        options={{
          tabBarIcon: ({ color, size }) => (
            <Ionicons name="person-circle-outline" size={24} color={color} />
          ),
        }}
      /> 
    </Tab.Navigator>
  );
}

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
          component={Tabs}
          options={{ headerShown: false }}
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