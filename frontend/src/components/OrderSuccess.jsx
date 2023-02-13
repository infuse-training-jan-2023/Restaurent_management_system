import React from 'react';
import { useState } from 'react';
import { Button, Result ,Modal} from 'antd';

const OrderMsg = ({show}) => 
{ 
  
  const [isModalOpen, setIsModalOpen] = useState(true);

  const showModal = () => {
    setIsModalOpen(current => !current);
  };
  return(
    <Modal open={isModalOpen} onCancel={showModal} footer={null}>
    <Result
    status="success"
    title="Order Successfull , Enjoy your meal!"
  />
</Modal>
)};

export default OrderMsg;