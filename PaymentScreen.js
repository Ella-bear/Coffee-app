import React, { useState } from 'react';
import { View, Text, Button } from 'react-native';
import axios from 'axios';
import { globalStyles } from '../styles';

const PaymentScreen = () => {
  const handlePayment = async (method) => {
    try {
      const response = await axios.post('http://localhost:8000/payment/1', { payment_method: method });
      alert(response.data.message);
    } catch (error) {
      alert('Payment failed');
    }
  };

  return (
    <View style={globalStyles.container}>
      <Text style={globalStyles.text}>Choose Payment Method</Text>
      <Button title="Card" onPress={() => handlePayment('card')} />
      <Button title="PayPal" onPress={() => handlePayment('paypal')} />
    </View>
  );
};

export default PaymentScreen;