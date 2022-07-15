export default function TransBox({ out }) {
  return (
    <textarea className="font-sans shadow" disabled={out}></textarea>
  );
};