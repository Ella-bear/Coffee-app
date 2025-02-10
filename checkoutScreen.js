import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, Button } from 'react-native';
import axios from 'axios';
import { globalStyles } from '../styles';

const CheckoutScreen = () => {
  const [cartItems, setCartItems] = useState([]);
  const [total, setTotal] = useState(0);

  useEffect(() => {
    const fetchCart = async () => {
      try {
        const response = await axios.get('http://localhost:8000/cart/1'); // Replace with actual user ID
        setCartItems(response.data);
        const totalAmount = response.data.reduce((acc, item) => acc + item.total_price, 0);
        setTotal(totalAmount);
      } catch (error) {
        console.error(error);
      }
    };
    fetchCart();
  }, []);

  const handleProceedToPayment = () => {
    if (cartItems.length === 0) {
      alert('Your cart is empty');
      return;
    }
    alert(`Proceeding to payment. Total: $${total}`);
  };

  return (
    <View style={globalStyles.container}>
      <Text style={globalStyles.text}>Checkout</Text>
      <FlatList
        data={cartItems}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View>
            <Text style={globalStyles.text}>{item.name} - ${item.total_price}</Text>
          </View>
        )}
      />
      <Text style={globalStyles.text}>Total: ${total.toFixed(2)}</Text>
      <Button title="Proceed to Payment" onPress={handleProceedToPayment} />
    </View>
  );
};

export default CheckoutScreen;