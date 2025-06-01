import React from 'react';
import { View, TextInput, StyleSheet, Text, TouchableOpacity } from 'react-native';
import { StackNavigationProp } from '@react-navigation/stack';

import Button from '../../components/Button';
import Input from '../../components/Input';
import {Pages} from '../../rotes/Navigation';

interface Props{
  navigation: StackNavigationProp<Pages>
}

const Register: React.FC<Props> = ({navigation}) => {
  const [username, setUsername] = React.useState<string>('');
  const [email, setEmail] = React.useState<string>('');
  const [password, setPassword] = React.useState<string>('');
  const [confirmPassword, setConfirmPassword] = React.useState<string>('');

  const create = () => {
    navigation.goBack();
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Novo Usúario</Text>
      <Input onChangeText={setUsername} placeholder="Usuário*" />
      <Input onChangeText={setEmail} placeholder="Email" />
      <Input onChangeText={setPassword} placeholder="Senha*" secureTextEntry />
      <Input onChangeText={setConfirmPassword} placeholder="Confirmar Senha*" secureTextEntry />

      <Button onPress={create} style={styles.create} text='Criar'/>
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
  title: {
    fontSize: 24,
    marginBottom: 20,
    color: '#fff',
  },
  login:{
    backgroundColor: '#eba417',
    marginRight: 10,
  },
  create:{
    backgroundColor: '#3EB489',
    marginLeft: 10,
  },
  buttonText:{
    fontWeight: 'bold',
    fontSize: 17,
  },
  buttonsRow:{
    flexDirection: 'row',
    justifyContent: 'space-between',
  },

});

export default Register;
