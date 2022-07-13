export default function TransBox({ out }) {
  return (
    <textarea className="font-mono shadow" disabled={out}></textarea>
  );
};