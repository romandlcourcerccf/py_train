from asyncio import Future

m_f = Future()

print(f"id done {m_f.done()}")

m_f.set_result(100)

print(f"id done {m_f.done()} and result is {m_f.result()}")
