import React, { useEffect, useState } from "react";

const Index = () => {
  const [showCursor, setShowCursor] = useState(true);

  useEffect(() => {
    const interval = setInterval(() => {
      setShowCursor((prev) => !prev);
    }, 500);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="text-green-500 font-mono bg-black min-h-screen flex flex-col items-start p-4">
      <h1 className="text-2xl mb-4">Welcome to Terminal Website</h1>
      <p className="mb-2">Type 'help' to see available commands.</p>
      <div className="flex">
        <span>$</span>
        <span className="ml-2">_</span>
        {showCursor && <span className="animate-blink">|</span>}
      </div>
    </div>
  );
};

export default Index;