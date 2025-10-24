from asyncio import Future

m_future = Future()

print(f'Is done ? {m_future.done()}')

m_future.set_result(33)

print(f'Is done ? {m_future.done()}')
