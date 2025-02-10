import React from 'react';
import { View, Text } from 'react-native';
import { globalStyles } from '../styles';

const ContactUsScreen = () => {
  return (
    <View style={globalStyles.container}>
      <Text style={globalStyles.text}>Contact Us</Text>
      <Text style={globalStyles.text}>Phone: +123-456-7890</Text>
      <Text style={globalStyles.text}>Email: support@coffeeapp.com</Text>
      <Text style={globalStyles.text}>Socials:</Text>
      <Text style={globalStyles.text}>Facebook: @CoffeeApp</Text>
      <Text style={globalStyles.text}>Instagram: @CoffeeApp</Text>
    </View>
  );
};

export default ContactUsScreen;