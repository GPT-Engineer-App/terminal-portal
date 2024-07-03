import React, { useEffect, useState } from "react";

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
      <h1 className="text-2xl mb-4">Welcome to Terminal Website</h1>
      <p className="mb-2">Type 'help' to see available commands.</p>
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
    </div>
  );
};

export default Index;