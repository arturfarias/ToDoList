import React from 'react';
import { View, TextInput, StyleSheet, Text, TouchableOpacity, ViewStyle, StyleProp } from 'react-native';

interface Props {
  onChangeText: (text: string) => void;
  style?: StyleProp<ViewStyle>;
  placeholder: string;
  secureTextEntry?: boolean;
}

const Input: React.FC<Props>=({onChangeText, style, placeholder, secureTextEntry})=>{
  return (
      <TextInput 
        style={[styles.input, style]}
        onChangeText={onChangeText}
        placeholder={placeholder}
        secureTextEntry={secureTextEntry}
        placeholderTextColor="#cccccc"/>
  );
};

const styles = StyleSheet.create({
  input: {
    width: '100%',
    backgroundColor: '#fff',
    padding: 12,
    borderRadius: 8,
    marginBottom: 15,
    fontWeight: 'bold',
  },
});

export default Input;
