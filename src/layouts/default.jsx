import { Outlet } from "react-router-dom";

const Layout = () => {
  return (
    <main className="flex flex-col min-h-screen p-4 overflow-auto items-start justify-start bg-black text-green-500 font-mono">
      <Outlet />
    </main>
  );
};

export default Layout;