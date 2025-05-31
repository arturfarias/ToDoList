import React from 'react';
import { View, TextInput, StyleSheet, Text, TouchableOpacity, ViewStyle, StyleProp } from 'react-native';

interface Props {
  onPress: () => void;
  style?: StyleProp<ViewStyle>;
  text: string
}

const Button: React.FC<Props>=({onPress, style, text})=>{
  return (
      <TouchableOpacity
        style={[styles.button, style]}
        activeOpacity={0.7}
        onPress={onPress}>
            <Text style={styles.buttonText}>{text}</Text>
      </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  button:{
    padding: 15,
    borderRadius: 7,
    alignItems: 'center',
    width: 150,
    height: 50,
  },
  buttonText:{
    fontWeight: 'bold',
    fontSize: 17,
  },
});

export default Button;
