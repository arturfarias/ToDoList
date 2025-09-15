import React, { useRef, useEffect, ReactNode } from 'react';
import { Animated, ViewStyle } from 'react-native';

interface AnimatedInputsProps {
  editMode: boolean;
  children: ReactNode;
  style?: ViewStyle | ViewStyle[];
  height?: number;
  duration?: number;
}

const AnimatedInputs: React.FC<AnimatedInputsProps> = ({
  editMode,
  children,
  style,
  height = 100,
  duration = 300,
}) => {
  const animation = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(animation, {
      toValue: editMode ? 1 : 0,
      duration,
      useNativeDriver: false,
    }).start();
  }, [editMode, duration, animation]);

  const animatedHeight = animation.interpolate({
    inputRange: [0, 1],
    outputRange: [0, height],
  });

  const opacity = animation;

  return (
    <Animated.View 
      style={[
        {
          height: animatedHeight,
          opacity,
          overflow: 'hidden',
          width: '100%',
          marginBottom: editMode ? 15 : 0,
        },
        style,
      ]}
    >
      {children}
    </Animated.View>
  );
};

export default AnimatedInputs;
