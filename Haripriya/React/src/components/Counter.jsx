import React from 'react'
import './App.css'
import { useState } from 'react'

const Counter = () => {
    const [count, setCount] = useState(0)
  return (
  
      <div className='box'>
    <h2>Count:{count}</h2>
    <button onClick={()=>setCount(count+1)}>Increment count</button>
   </div>
    
  )
}

export default Counter
