import React, { useState } from 'react';
import TransBox from './TransBox';

export default function TransContainer() {
  const [text, setText] = useState("hello");
  const onChange = (newText) => {
    setText(newText);
  };
  
  return (
    <>
      <TransBox text={text} onChange={onChange}/>
      <TransBox out text={text} onChange={onChange}/>
    </>
  );
}
