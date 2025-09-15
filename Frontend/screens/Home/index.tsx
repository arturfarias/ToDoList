import React from 'react';
import { View, StyleSheet, Text } from 'react-native';
import { StackNavigationProp } from '@react-navigation/stack';
import {PagesStack} from '../../rotes/Navigation';

interface Props{
  navigation: StackNavigationProp<PagesStack>
}

const Home: React.FC<Props> = ({navigation}) => {

  return (
    <View style={styles.container}>
        <Text>Tela de Home muito bonita</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#6a0dad',
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 20,
  },
});

export default Home;
