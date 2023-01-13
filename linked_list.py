from __future__ import annotations
from typing import Any,Type

class Node:
	"""연결 리스트용 노드 클래스"""
	def __init__(self, data: Any = None, next: Node = None):
		self.data = data #데이터
		self.next = next #뒤쪽 포인터

class LinkedList:
	def __init__(self) -> None:
		self.no = 0 #리스트에 등록되어 있는 노드의 개수
		self.head = None #머리 노드에 대한 참조
		self.current = None #현재 주목하고 있는 노드에 대한 참조(노드 검색 후 삭제하는 등의 용도)
	
	def __len__(self) -> int:
		#노드 개수 반환
		return self.no 
	
	def search(self, data: Any) -> int:
		cnt = 0
		ptr = self.head
		while ptr is not None:
			if ptr.data == data:
				self.current = ptr
				return cnt
			cnt += 1
			ptr = ptr.next
		return -1

	def __contains__(self, data: Any)-> bool:
		return self.search(data) >= 0
	
	def add_first(self, data: Any) -> None:
		ptr = self.head
		self.head = self.current = Node(data, ptr)
		self.no += 1

	def add_last(self, data: Any):
		if self.head is None:
			self.add_first(data)
		else:
			ptr = self.head
			while ptr.next is not None:
				ptr = ptr.next
			ptr.next = self.current = Node(data, None)
			self.no += 1
	
	def remove_first(self)-> None:
		if self.head is not None:
			self.head = self.current = self.head.next
		self.no = -1

	def remove_last(self) -> None:
		if self.head is not None:
			if self.head.next is None: #노드가 1개라면
				self.remove_first() #머리노드 삭제
			else:
				ptr = self.head #스캔 중인 노드
				ptr = self.head #스캔 중인 노드의 앞쪽 노드

				while ptr.next is not None:
					pre = ptr
					ptr = ptr.next
				pre.next = None #pre는 삭제 뒤 꼬리 노드
				self.current = pre
				self.no -= 1
	
	#임의의 노드 삭제
	def remove(self, p: Node) -> None:
		'''노드 p를 삭제'''
		if self.head is not None:
			if p in self.head: #p가 머리 노드이면
				self.remove_first() #머리 노드를 삭제
			else:
				ptr = self.head

				while ptr.next is not p:
					ptr = ptr.next
					if ptr is None:
						return 
				
				ptr.next = p.next
				self.current = ptr
				self.no -= 1
	
	def remove_current_node(self) -> None:
		self.remove(self.current)

	def clear(self) -> None:
		while self.head is not None: #전체가 비어 있을 떄까지
			self.remove_first() #머리 노드를 삭제
		self.current = None
		self.no = 0

	def next(self) -> bool:
		#주목 노드를 한 칸 뒤로 이동
		if self.current is None or self.current.next is None:
			return False #이동할 수 없음
		self.current = self.current.next
		return True

	def print_current_node(self) -> None:
		if self.current is None:
			print('주목 노드가 존재하지 않습니다.')
		else:
			print(self.current.data)

	def print(self) -> None:
		ptr = self.head

		while ptr is not None:
			print(ptr.data)
			ptr = ptr.next
			
	#이터레이터용 클래스 구현
	def __iter__(self) -> LinkedListIterator:
		return LinkedListIterator(self.head)

class LinkedListIterator:
	def __init__(self, head: Node):
		self.current = head
	
	def __iter__(self) -> LinkedListIterator:
		return self
	
	def __next__(self) -> Any:
		if self.current is None:
			raise StopIteration
		else:
			data = self.current.data
			self.current = self.current.next
			return data