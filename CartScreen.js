import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, TouchableOpacity } from 'react-native';
import axios from 'axios';
import { globalStyles } from '../styles';

const CartScreen = () => {
  const [cartItems, setCartItems] = useState([]);

  useEffect(() => {
    const fetchCart = async () => {
      const response = await axios.get('http://localhost:8000/cart/1'); // Replace with user ID
      setCartItems(response.data);
    };
    fetchCart();
  }, []);

  const handleRemove = async (id) => {
    await axios.delete(`http://localhost:8000/remove-from-cart/${id}`);
    alert('Item removed');
    setCartItems(cartItems.filter((item) => item.id !== id));
  };

  return (
    <View style={globalStyles.container}>
      <FlatList
        data={cartItems}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View>
            <Text style={globalStyles.text}>{item.name} - ${item.total_price}</Text>
            <TouchableOpacity onPress={() => handleRemove(item.id)}>
              <Text>Remove</Text>
            </TouchableOpacity>
          </View>
        )}
      />
    </View>
  );
};

export default CartScreen;