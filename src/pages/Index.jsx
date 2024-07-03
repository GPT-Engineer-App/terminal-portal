import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const Index = () => {
  const [showCursor, setShowCursor] = useState(true);
  const [input, setInput] = useState("");
  const [output, setOutput] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      setShowCursor((prev) => !prev);
    }, 500);
    return () => clearInterval(interval);
  }, []);

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleInputSubmit = (e) => {
    if (e.key === "Enter") {
      setOutput((prevOutput) => [...prevOutput, input]);
      setInput("");
    }
  };

  return (
    <div className="text-green-500 font-mono bg-black min-h-screen flex flex-col items-start p-4">
      <pre className="text-2xl mb-4">
        {`
        ___ ___    __    __  .__   __.  _______ .__   __.  __    __       ___       __  ___  _______ .___  ___.  _______ 
       /   |   \\  |  |  |  | |  \\ |  | |   ____||  \\ |  | |  |  |  |     /   \\     |  |/  / |   ____||   \\/   | |   ____|
      /  ^  ^   \\ |  |  |  | |   \\|  | |  |__   |   \\|  | |  |  |  |    /  ^  ^    \\|  '  /  |  |__   |  \\  /  | |  |__   
     /  /_/_\\  \\ |  |  |  | |  . \`  | |   __|  |  . \`  | |  |  |  |   /  /_/_\\  \\    |    <   |   __|  |  |\\/|  | |   __|  
    /  _____  \\ |  \`--'  | |  |\\   | |  |____ |  |\\   | |  \`--'  |  /  _____  \\   |  .  \\  |  |____ |  |  |  | |  |____ 
   /__/     \\__\\ \\______/  |__| \\__| |_______||__| \\__|  \\______/  /__/     \\__\\  |__|\\__\\ |_______||__|  |__| |_______|
        `}
      </pre>
      <div className="flex flex-col w-full">
        {output.map((line, index) => (
          <div key={index} className="flex">
            <span>$</span>
            <span className="ml-2">{line}</span>
          </div>
        ))}
        <div className="flex">
          <span>$</span>
          <input
            type="text"
            value={input}
            onChange={handleInputChange}
            onKeyDown={handleInputSubmit}
            className="bg-black text-green-500 outline-none ml-2 flex-grow"
            autoFocus
          />
          {showCursor && <span className="animate-blink">|</span>}
        </div>
      </div>
      <div className="mt-4">
        <p>1. <Link to="/about" className="text-green-500 hover:underline">About</Link></p>
        <p>2. <Link to="/vision" className="text-green-500 hover:underline">Vision</Link></p>
        <p>3. <Link to="/careers" className="text-green-500 hover:underline">Careers</Link></p>
      </div>
    </div>
  );
};

export default Index;